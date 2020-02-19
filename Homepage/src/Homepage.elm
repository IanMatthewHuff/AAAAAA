module Homepage exposing (main)

import Html exposing (..)
import Html.Attributes exposing (..)


view model =
    div [ class "jumbotron" ]
        [ h1 [] [ text "Automated Abstract Art Assembly And Appreciation" ]
        , p []
            [ text "text"
            , strong [] [ text "AAAAAA" ]
            , text <|
                """ 
                First in art. First in the Yellow Pages.
                """
            ]
        ]


main =
    view "dummy model"
