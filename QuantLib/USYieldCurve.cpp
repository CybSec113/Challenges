#include <ql/qldefines.hpp>
#if !defined(BOOST_ALL_NO_LIB) && defined(BOOST_MSVC)
#  include <ql/auto_link.hpp>
#endif

#include <ql/termstructures/yield/fittedbonddiscountcurve.hpp>
#include <ql/termstructures/yield/piecewiseyieldcurve.hpp>
#include <ql/time/calendars/unitedstates.hpp>
#include <ql/time/daycounters/actual365fixed.hpp>
#include <ql/pricingengines/bond/bondfunctions.hpp>
#include <ql/utilities/dataformatters.hpp>
#include <ql/settings.hpp>

#include <iostream>
#include <iomanip>

// a useful macro
#define LENGTH(a) (sizeof(a)/sizeof(a[0]))

using namespace QuantLib;
using namespace std;

int main(int, char* []) {

    try {
        cout << "Hello, QuantLib!" << endl;

        // Reference Data
        Natural treasSettlementDays = 1;
        DayCounter treasDayCount = Actual365Fixed();
        Frequency treasFreq = Semiannual;
        BusinessDayConvention treasBDay = ModifiedFollowing;
        Calendar treasCalendar = UnitedStates(UnitedStates::GovernmentBond);

        cout << setfill('-') << left;
        cout << setw(20) << "-" << "Reference Data" << setw(20) << "-" << endl;
        cout << setfill('.');
        cout << setw(30) << "Treasury Settlement Days" << treasSettlementDays << endl;
        cout << setw(30) << "Treasury Day Count Conv" << treasDayCount << endl;
        cout << setw(30) << "Treasury Cpn Freq" << treasFreq << endl;
        cout << setw(30) << "Treasury B-Day Conv" << treasBDay << endl;
        cout << setw(30) << "Treasury Calendar" << treasCalendar << endl;
        cout << endl;

        // Market data
        Integer ontherunMats[] =    {2,5,10,30};
        Integer offtherunMats[] =   {3,4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29};
        Real ontherunCpns[] =       {0.045, 0.040, 0.040, 0.045, 0.0425};
        Real ontherunPx[] =         {100.0,100.0,100.0,100.0,100.0};
        Date today = treasCalendar.adjust(Date::todaysDate());
        Date treasSettleDate = treasCalendar.advance(today, treasSettlementDays*Days);

        cout << setfill('-') << left;
        cout << setw(20) << "-" << "Market Data" << setw(20) << "-" << endl;
        cout << setfill('.');
        cout << setw(30) << "On The Run Maturities";
        for (Integer& mats : ontherunMats) cout << setfill('\0') << mats << ", ";
        cout << setfill('.') << endl;
        cout << setw(30) << "On The Run Coupons";
        for (Real& cpns : ontherunCpns) cout << setfill('\0') << setprecision(3) << io::percent(cpns) << ", ";
        cout << setfill('.') << endl;
        cout << setw(30) << "Today" << io::short_date(today) << endl;
        cout << setw(30) << "Treasury Settlement Date" << io::short_date(treasSettleDate) << endl;
        cout << endl;

        // Model data
        Settings::instance().evaluationDate() = today;
        cout << setfill('-') << left;
        cout << setw(20) << "-" << "Model Data" << setw(20) << "-" << endl;
        cout << setfill('.');
        cout << setw(30) << "Evaluation Date" << io::short_date(today) << endl;
        cout << endl;

        // Start building curve

        // This will set up initial quotes as Handles needed for building the curve
        std::vector<ext::shared_ptr<SimpleQuote>> quote;
        for (Real qt : ontherunPx)
            quote.push_back(ext::make_shared<SimpleQuote>(qt));
        
        RelinkableHandle<Quote> quoteHandle[LENGTH(ontherunMats)];
        for (Size i=0; i<LENGTH(ontherunMats); i++)
            quoteHandle[i].linkTo(quote[i]);

        std::vector<ext::shared_ptr<BondHelper>> bondsInst;
        std::vector<ext::shared_ptr<RateHelper>> ratesInst;

        // this will add bonds and corresponding rates to the instrument vectors
        for (Size i=0; i<LENGTH(ontherunMats); i++) {
            Date matDate = treasCalendar.advance(treasSettleDate, ontherunMats[i]*Years);
            Schedule treasSched(treasSettleDate, matDate, Period(treasFreq), treasCalendar, treasBDay, treasBDay, DateGeneration::Backward, false);

            auto bondHelper = ext::make_shared<FixedRateBondHelper>(quoteHandle[i],
                                                treasSettlementDays,
                                                100.0,
                                                treasSched,
                                                std::vector<Rate>(1,ontherunCpns[i]),
                                                treasDayCount,
                                                treasBDay,
                                                100.0);

            auto rateHelper = ext::make_shared<FixedRateBondHelper>(quoteHandle[i],
                                                treasSettlementDays,
                                                100.0,
                                                treasSched,
                                                std::vector<Rate>(1,ontherunCpns[i]),
                                                treasDayCount,
                                                treasBDay,
                                                100.0);
            bondsInst.push_back(bondHelper);
            ratesInst.push_back(rateHelper);
        }

        // This will build the actual curve
        // Traits: Discount, ZeroYield, ForwardRate, SimpleZeroYield
        // Interpolation type: https://rkapl123.github.io/QLAnnotatedSource/d6/d86/group__interpolations.html
        auto treasCurve01 = ext::make_shared<PiecewiseYieldCurve<Discount, LogLinear>>(treasSettlementDays,
                                                                    treasCalendar,
                                                                    ratesInst,
                                                                    treasDayCount);
        cout << "Treasury Curve 01: Piecewise Yield Curve: Discount, LogLinear" << endl;
        cout << "Reference Date: " << treasCurve01->referenceDate() << endl;
        for (std::pair<Date,Real>& i : treasCurve01->nodes()) {
            cout << io::short_date(i.first) << " ";
            cout << io::percent(i.second) << endl;
        }
        cout << endl;

    } catch (std::exception& e) {
        std::cerr << e.what() << std::endl;
        return 1;
    } catch (...) {
        std::cerr << "unknown error" << std::endl;
        return 1;
    }
}