people_award = {}

film_award = {}

film_award['best screenplay - motion picture'] = (r'[Bb]est [Ss]creenplay')

people_award['best director - motion picture'] = (r'[Bb]est [Dd]irector')

people_award['best performance by an actress in a television series - comedy or musical'] = (r'[Bb]est [Pp]erformance.*[Aa]ctress.*[Tt].*[Vv].* [Mm]usical')

film_award['best foreign language film'] = (r'[Ff]oreign [Ll]anguage [Ff]ilm')


people_award['best performance by an actor in a supporting role in a motion picture'] = (r'([Aa]ct[oe]r.*[Ss]upporting|[Ss]upporting [Aa]ct[oe]r).*(in a|in).*[Mm]otion.*')

people_award['best performance by an actress in a supporting role in a series, mini-series or motion picture made for television'] = (r'([Ss]upporting.*[Aa]ctress.*[Ss]eries|[Aa]ctress.*[Ss]upporting [Rr]ole.*[Ss]eries)')

film_award['best motion picture - comedy or musical'] = (r'[Bb]est [Mm]otion [Pp]icture .*[Co]medy.*[Mm]usical')

people_award['best performance by an actress in a motion picture - comedy or musical'] = (r'[Bb]est [Pp]erformance.*[Aa]ctress.*[Mm]otion [Pp]icture.*[Cc]omedy.*[Mu]sical')

film_award['best mini-series or motion picture made for television'] = (r'[Bb]est [Mm]ini.*[Ss]eries .*[Mm]otion [Pp]icture.*([Tt][Vv]|[Tt]elevision)')

film_award['best original score - motion picture '] = (r'[Bb]est [Oo]riginal [Ss]core.*[Mm]otion [Pp]icture')

people_award['best performance by an actress in a television series - drama'] = (r'[Bb]est.*[Aa]ctress.*([Tt][Vv]|[Tt]elevision).*[Dd]rama')

people_award['# best performance by an actress in a motion picture - drama'] = (r'[Bb]est.*[Aa]ctress.*[Mm]otion [Pp]icture.*[Dd]rama')

people_award['cecil b. demille award'] = (r'[Cc]ecil.*[Dd]emille')

people_award['best performance by an actor in a motion picture - comedy or musical'] = (r'[Bb]est [Pp]erformance.* [Aa]ct[oe]r.*[Mm]otion [Pp]icture.*[Cc]omedy')

people_award['best performance by an actor in a supporting role in a series, mini-series or motion picture made for television'] = (r'([Aa]ctor.*[Ss]upporting|[Ss]upporting.*[Aa]ctor).*[Rr]ole.*[Mm]ini')

people_award[' best performance by an actress in a supporting role in a motion picture'] = (r'([Ss]upporting [Aa]ctress|[Aa]ctress.*[Ss]upporting).*([Mm]otion [Pp]icture|[Ff]ilm)')

film_award[' best motion picture - drama'] = (r'([Bb]est|[Ll]eading) ((([Mm]otion)?\s?[Pp]icture|[Ff]ilm).*[Dd]rama|[Dd]rama.*(([Mm]otion)? [Pp]icture|[Ff]ilm))')

film_award['best television series - drama'] = (r'([Bb]est|[Ll]eading) (([Tt][Vv]|[Ss]eries).*[Dd]rama|([Tt][Vv]|[Ss]eries)|[Dd]rama [Ss]eries)')

people_award[' best performance by an actor in a mini-series or motion picture made for television'] = (r'([Bb]est|[Ll]eading).*[Aa]ctor.*[Mm]ini.*[Tt].*[Vv]')

people_award['best performance by an actress in a mini-series or motion picture made for television'] = (r'([Bb]est|[Ll]eading).*[Aa]ctress.*[Mm]ini.*[Tt].*[Vv]')

film_award[' best animated feature film'] = (r'[Bb]est [Aa]nimated')

film_award['best original song - motion picture'] = (r'[Bb]est ([Oo]riginal )?[Ss]ong')

people_award[' best performance by an actor in a motion picture - drama '] = (r'[Aa]ct[oe]r.*(([Mm]otion)[Pp]icture|[Ff]ilm).*([Dd]rama)')

film_award[' best television series - comedy or musical'] = (r'[Bb]est ([Tt][Vv]|[Tt]elevision).*[Cc]omedy')

people_award['best performance by an actor in a television series - drama'] = (r'[Aa]ct[oe]r( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*[Dd]rama')

people_award['best performance by an actor in a television series - comedy or musical'] = (r'[Aa]ct[oe]r( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*[Cc]omedy')