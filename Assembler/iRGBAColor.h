/*

iRGBAColor.h

iRGBAColor is the interface for any assembler stage that provides a number of RGBA colors

*/
#pragma once

#include "stdafx.h"

namespace AAAAAA
{
    namespace Assembler
    {
        struct RGBAColor
        {
            public:
                int R;
                int G;
                int B;
                int A;
        };

        class IRGBAColor
        {
            public:
                virtual bool GetColors(const int numberRequested, std::list<RGBAColor>& colors) = 0;    
        };
    }
}
