class Regex:
  def __init__(self):
    self.award_names = [' best screenplay - motion picture ',' best director - motion picture ',' best performance by an actress in a television series - comedy or musical ',' best foreign language film ',' best performance by an actor in a supporting role in a motion picture ',' best performance by an actress in a supporting role in a series, mini-series or motion picture made for television ',' best motion picture - comedy or musical ',' best performance by an actress in a motion picture - comedy or musical ',' best mini-series or motion picture made for television ',' best original score - motion picture ',' best performance by an actress in a television series - drama ',' best performance by an actress in a motion picture - drama ',' cecil b. demille award ',' best performance by an actor in a motion picture - comedy or musical ',' best motion picture - drama ',' best performance by an actor in a supporting role in a series, mini-series or motion picture made for television ',' best performance by an actress in a supporting role in a motion picture ',' best television series - drama ',' best performance by an actor in a mini-series or motion picture made for television ',' best performance by an actress in a mini-series or motion picture made for television ',' best animated feature film ',' best original song - motion picture ',' best performance by an actor in a motion picture - drama ',' best television series - comedy or musical ',' best performance by an actor in a television series - drama ',' best performance by an actor in a television series - comedy or musical ']
    self.award_dict = {}
    # to do: fuzzy search for the award name

    # best screenplay - motion picture 
    self.award_dict['best screenplay - motion picture'] = (r'[Bb]est [Ss]creenplay')
    # self.award_dict['best screenplay - motion picture'] = (r'[Bb]est [Sc]reenplay')

    # best director - motion picture
    self.award_dict['best director - motion picture'] = (r'[Bb]est [Dd]irector')

    # best performance by an actress in a television series - comedy or musical 
    self.award_dict['best performance by an actress in a television series - comedy or musical'] = (r'[Bb]est [Pp]erformance .* [Aa]ctress .* [Tt][Vv].* [Mm]usical')

    # best foreign language film 
    self.award_dict['best foreign language film'] = (r'[Ff]oreign [Ll]anguage [Ff]ilm')

    # best performance by an actor in a supporting role in a motion picture
    # ONLY RETURNS ONE RESULT
    self.award_dict['best performance by an actor in a supporting role in a motion picture'] = (r'([Aa]ct[oe]r.*[Ss]upporting|[Ss]upporting [Aa]ct[oe]r) (in a|in) [Mm]otion')

    # best performance by an actress in a supporting role in a series, mini-series or motion picture made for television
    self.award_dict['best performance by an actress in a supporting role in a series, mini-series or motion picture made for television'] = (r'([Ss]upporting.*[Aa]ctress.*[Ss]eries|[Aa]ctress.*[Ss]upporting [Rr]ole.*[Ss]eries)')

    #best motion picture - comedy or musical 
    self.award_dict['best motion picture - comedy or musical'] = (r'[Bb]est [Mm]otion [Pp]icture .*[Co]medy .* [Mm]usical')

    # best performance by an actress in a motion picture - comedy or musical
    # 5 RESULTS
    self.award_dict['best performance by an actress in a motion picture - comedy or musical'] = (r'[Bb]est [Pp]erformance .* [A]ctress [Ii]n [Aa] [Mm]otion [Pp]icture.*[Cc]omedy')

    # best mini-series or motion picture made for television
    self.award_dict['best mini-series or motion picture made for television'] = (r'[Bb]est [Mm]ini.*[Ss]eries .*[Mm]otion [Pp]icture.*([Tt][Vv]|[Tt]elevision)')

    # best original score - motion picture 
    self.award_dict['best original score - motion picture '] = (r'[Bb]est [Oo]riginal [Ss]core.*[Mm]otion [Pp]icture')

    # best performance by an actress in a television series - drama
    self.award_dict['best performance by an actress in a television series - drama'] = (r'[Bb]est [Aa]ctress( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*[Dd]rama')

    # best performance by an actress in a motion picture - drama 
    self.award_dict['# best performance by an actress in a motion picture - drama'] = (r'[Bb]est [Aa]ctress.*[Mm]otion [Pp]icture.*[Dd]rama')

    # cecil b. demille award 
    self.award_dict['cecil b. demille award'] = (r'[Cc]ecil.*[Dd]emille')

    # best performance by an actor in a motion picture - comedy or musical
    self.award_dict['best performance by an actor in a motion picture - comedy or musical'] = (r'[Bb]est [Pp]erformance .* [Aa]ct[oe]r.* [Mm]otion [Pp]icture.*[Cc]omedy')

    # best performance by an actor in a supporting role in a series, mini-series or motion picture made for television 
    self.award_dict['best performance by an actor in a supporting role in a series, mini-series or motion picture made for television'] = (r'[Ss]upporting.*[Aa]ct[oe]r.*[Mm]ini')

    #  best performance by an actress in a supporting role in a motion picture
    self.award_dict['best performance by an actress in a supporting role in a motion picture'] = (r'([Bb]est|[Ll]eading) ([Ss]upporting [Aa]ctress|[Aa]ctress.*[Ss]upporting).*([Mm]otion [Pp]icture|[Ff]ilm)')

    #  best motion picture - drama 
    self.award_dict['best motion picture - drama'] = (r'([Bb]est|[Ll]eading) ((([Mm]otion)?\s?[Pp]icture|[Ff]ilm).*[Dd]rama|[Dd]rama.*(([Mm]otion)? [Pp]icture|[Ff]ilm))')

    #  best television series - drama 
    self.award_dict['best television series - drama'] = (r'([Bb]est|[Ll]eading) (([Tt][Vv]|[Ss]eries).*[Dd]rama|([Tt][Vv]|[Ss]eries)|[Dd]rama [Ss]eries)')

    # best performance by an actor in a mini-series or motion picture made for television 
    self.award_dict['best performance by an actor in a mini-series or motion picture made for television'] = (r'([Bb]est|[Ll]eading) [Aa]ctor.*[Mm]ini')

    # best performance by an actress in a mini-series or motion picture made for television 
    self.award_dict['best performance by an actress in a mini-series or motion picture made for television'] = (r'([Bb]est|[Ll]eading) [Aa]ctress.*[Mm]ini')

    #  best animated feature film 
    self.award_dict['best animated feature film'] = (r'[Bb]est [Aa]nimated')

    #  best original song - motion picture 
    self.award_dict['best original song - motion picture'] = (r'[Bb]est ([Oo]riginal )?[Ss]ong')

    # best performance by an actor in a motion picture - drama 
    self.award_dict['best performance by an actor in a motion picture - drama '] = (r'[Bb]est [Aa]ct[oe]r.*(([Mm]otion)?\s?[Pp]icture|[Ff]ilm).*([Dd]rama)?')

    # best television series - comedy or musical 
    self.award_dict['best television series - comedy or musical'] = (r'[Bb]est ([Tt][Vv]|[Tt]elevision).*[Cc]omedy')

    # best performance by an actor in a television series - drama
    self.award_dict['best performance by an actor in a television series - drama'] = (r'[Bb]est [Aa]ct[oe]r( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*[Dd]rama')

    # best performance by an actor in a television series - comedy or musical
    self.award_dict['best performance by an actor in a television series - comedy or musical'] = (r'[Bb]est [Aa]ct[oe]r( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*[Cc]omedy')

    

  def getRegex(self, key):
    if key in self.award_dict:
      return self.award_dict[key]
    else: 
      return False

reg = Regex()
# print(reg.getRegex("best animated feature film"))