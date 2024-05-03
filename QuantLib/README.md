## What

Self-study in QuantLib and boost C++ libraries.

## Why

Pursuing a technology career that also leverages my experience in risk management.

## How

1) Install boost and QuantLib.  
2) Review some of the examples provided, including FittedBondCurve.cpp and Bonds.cpp 
3) configure --with-boost-include=/opt/homebrew/include/ \
            --prefix=${HOME}/local/ \
            CXXFLAGS='-O2 -stdlib=libc++ -mmacosx-version-min=10.9' \
            LDFLAGS='-stdlib=libc++ -mmacosx-version-min=10.9'
4) Compile using the recommended approach: ``g++ `/usr/local/opt/quantlib/bin/quantlib-config --cflags` USYieldCurve.cpp -o USYieldCurve `/usr/local/opt/quantlib/bin/quantlib-config --libs` ``