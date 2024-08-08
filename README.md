Building out a repository of Python and C++ coding examples.  This is 100% self-study becuase I really enjoy solving problems through writing code.

HackerRank, LeetCode, and Meta directories include solutions to programming "challenges".

QuantLib directory includes a sample of a zero coupon yield curve.  Through this example, I was able to reinforce knowledge of C++ Standard Template Library and learned how to utilize boost tools.

I am currency working on two other projects:
* Installing a self-contained web server (Apache2) on a Raspberry Pi 4 with a seb site (Djanog) that updates sensor hat data in real time.
* Writing a VS Code extenstion (TypeScript) that integrates with Unix Password Store.

I recently contributed my first [update](https://github.com/justinsgithub/terminal-typing-tutor/pull/8#issue-2438829356) to a project on GitHub. I added a Quote of the Day Lesson to a terminal typing tutor. It can be installed by running: `pip install terminal-typing-tutor`. I strongly recommend creating a virtual Python environment for ease of installation, details [here](https://github.com/pyenv/pyenv.git).


# For QuantLib:
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