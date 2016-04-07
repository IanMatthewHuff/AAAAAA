/* 

AssemblerStage is the base class for a single stage in the AAAAAA Assembler program.

This base class provides the functionality common to all assembler stages, which inherit from this
and from any of the virtual interfaces for the functionality that they implement

*/

#pragma once

#include "stdafx.h"

namespace AAAAAA
{
    namespace Assembler
    {
        class AssemblerStage
        {
            public:
                AssemblerStage();

                // This string will be used as the ID of each stage in the pipeline process
                virtual std::wstring StageName() = 0;
        };        
    }
}
