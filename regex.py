class Regex:
  def __init__(self):
    self.award_names = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
    self.award_dict = {}
    self.people_award = {}
    self.film_award = {}
    # to do: fuzzy search for the award name

    # best screenplay - motion picture 
    self.award_dict['best screenplay - motion picture'] = (r'[Bb]est [Ss]creenplay')

    # best director - motion picture
    self.award_dict['best director - motion picture'] = (r'[Bb]est [Dd]irector')

    # best performance by an actress in a television series - comedy or musical 
    self.award_dict['best performance by an actress in a television series - comedy or musical'] = (r'[Bb]est.* [Aa]ctress .*([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')
    self.award_dict['best performance by an actress in a television series - musical or comedy'] = (r'[Bb]est.* [Aa]ctress .*([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')

    # best foreign language film 
    self.award_dict['best foreign language film'] = (r'[Bb]est [Ff]oreign [Ll]anguage [Ff]ilm')
    self.award_dict['best motion picture - foreign language'] = (r'[Bb]est.*[Ff]oreign [Ll]anguage')

    # best performance by an actor in a supporting role in a motion picture
    # ONLY RETURNS ONE RESULT
    self.award_dict['best performance by an actor in a supporting role in a motion picture'] = (r'([Aa]ct[oe]r.*[Ss]upporting|[Ss]upporting [Aa]ct[oe]r) (in a|in) [Mm]otion')
    self.award_dict['best performance by an actor in a supporting role in any motion picture'] = (r'([Aa]ct[oe]r.*[Ss]upporting|[Ss]upporting [Aa]ct[oe]r) (in any|in|in a) [Mm]otion')

    # best performance by an actress in a supporting role in a series, mini-series or motion picture made for television
    self.award_dict['best performance by an actress in a supporting role in a series, mini-series or motion picture made for television'] = (r'([Ss]upporting.*[Aa]ctress.*[Ss]eries|[Aa]ctress.*[Ss]upporting [Rr]ole.*[Ss]eries)')
    self.award_dict['best performance by an actress in a supporting role in a series, limited series or motion picture made for television'] = (r'([Ss]upporting.*[Aa]ctress.*[Ss]eries|[Aa]ctress.*[Ss]upporting [Rr]ole.*[Ss]eries)')

    #best motion picture - comedy or musical 
    self.award_dict['best motion picture - comedy or musical'] = (r'[Bb]est [Mm]otion [Pp]icture .*([Cc]omedy|[Mm]usical)')
    self.award_dict['best motion picture - musical or comedy'] = (r'[Bb]est [Mm]otion [Pp]icture .*([Cc]omedy|[Mm]usical)')
    
    # best performance by an actress in a motion picture - comedy or musical
    # 5 RESULTS
    self.award_dict['best performance by an actress in a motion picture - comedy or musical'] = (r'[Bb]est.* [A]ctress [Ii]n [Aa] [Mm]otion [Pp]icture.*([Cc]omedy|[Mm]usical)')
    self.award_dict['best performance by an actress in a motion picture - musical or comedy'] = (r'[Bb]est.* [A]ctress [Ii]n [Aa] [Mm]otion [Pp]icture.*([Cc]omedy|[Mm]usical)')
    

    # best mini-series or motion picture made for television
    self.award_dict['best mini-series or motion picture made for television'] = (r'[Bb]est [Mm]ini.*[Ss]eries .*[Mm]otion [Pp]icture.*([Tt][Vv]|[Tt]elevision)')

    # best original score - motion picture 
    self.award_dict['best original score - motion picture'] = (r'[Bb]est [Oo]riginal [Ss]core.*[Mm]otion [Pp]icture')

    # best performance by an actress in a television series - drama
    self.award_dict['best performance by an actress in a television series - drama'] = (r'[Bb]est.*[Aa]ctress( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*[Dd]rama')

    # best performance by an actress in a motion picture - drama 
    self.award_dict['best performance by an actress in a motion picture - drama'] = (r'[Bb]est.*[Aa]ctress.*[Mm]otion [Pp]icture.*[Dd]rama')

    # cecil b. demille award 
    self.award_dict['cecil b. demille award'] = (r'[Cc]ecil.*[Dd]emille')

    # best performance by an actor in a motion picture - comedy or musical
    self.award_dict['best performance by an actor in a motion picture - comedy or musical'] = (r'[Bb]est.* [Aa]ct[oe]r.* [Mm]otion [Pp]icture.*([Cc]omedy|[Mm]usical)')
    self.award_dict['best performance by an actor in a motion picture - musical or comedy'] = (r'[Bb]est.* [Aa]ct[oe]r.* [Mm]otion [Pp]icture.*([Cc]omedy|[Mm]usical)')

    # best performance by an actor in a supporting role in a series, mini-series or motion picture made for television 
    self.award_dict['best performance by an actor in a supporting role in a series, mini-series or motion picture made for television'] = (r'[Ss]upporting.*[Aa]ct[oe]r.*[Mm]ini')
    self.award_dict['best performance by an actor in a supporting role in a series, limited series or motion picture made for television'] = (r'[Ss]upporting.*[Aa]ct[oe]r.*([Mm]ini|[Ll]imited)')

    #  best performance by an actress in a supporting role in a motion picture
    self.award_dict['best performance by an actress in a supporting role in a motion picture'] = (r'([Bb]est|[Ll]eading) ([Ss]upporting [Aa]ctress|[Aa]ctress.*[Ss]upporting).*([Mm]otion [Pp]icture|[Ff]ilm)')
    self.award_dict['best performance by an actress in a supporting role in any motion picture'] = (r'([Bb]est|[Ll]eading) ([Ss]upporting [Aa]ctress|[Aa]ctress.*[Ss]upporting).*([Mm]otion [Pp]icture|[Ff]ilm)')

    #  best motion picture - drama 
    self.award_dict['best motion picture - drama'] = (r'([Bb]est|[Ll]eading) ((([Mm]otion)?\s?[Pp]icture|[Ff]ilm).*[Dd]rama|[Dd]rama.*(([Mm]otion)? [Pp]icture|[Ff]ilm))')

    #  best television series - drama 
    self.award_dict['best television series - drama'] = (r'([Bb]est|[Ll]eading) (([Tt][Vv]|[Ss]eries).*[Dd]rama|([Tt][Vv]|[Ss]eries)|[Dd]rama [Ss]eries)')

    # best performance by an actor in a mini-series or motion picture made for television 
    self.award_dict['best performance by an actor in a mini-series or motion picture made for television'] = (r'([Bb]est|[Ll]eading) [Aa]ctor.*[Mm]ini')
    self.award_dict['best performance by an actor in a limited series or a motion picture made for television'] = (r'([Bb]est|[Ll]eading) [Aa]ctor.*([Mm]ini|[Ll]imited)')

    # best performance by an actress in a mini-series or motion picture made for television 
    self.award_dict['best performance by an actress in a mini-series or motion picture made for television'] = (r'([Bb]est|[Ll]eading) [Aa]ctress.*[Mm]ini')
    self.award_dict['best performance by an actress in a limited series or a motion picture made for television'] = (r'([Bb]est|[Ll]eading) [Aa]ctress.*([Mm]ini|[Ll]imited)')

    #  best animated feature film 
    self.award_dict['best animated feature film'] = (r'[Bb]est [Aa]nimated')
    self.award_dict['best motion picture - animated'] = (r'[Bb]est.*[Aa]nimated')

    #  best original song - motion picture 
    self.award_dict['best original song - motion picture'] = (r'[Bb]est ([Oo]riginal )?[Ss]ong')

    # best performance by an actor in a motion picture - drama 
    self.award_dict['best performance by an actor in a motion picture - drama'] = (r'[Bb]est [Aa]ct[oe]r.*(([Mm]otion)?\s?[Pp]icture|[Ff]ilm).*([Dd]rama)?')

    # best television series - comedy or musical 
    self.award_dict['best television series - comedy or musical'] = (r'[Bb]est ([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')
    self.award_dict['best television series - musical or comedy'] = (r'[Bb]est ([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')

    # best performance by an actor in a television series - drama
    self.award_dict['best performance by an actor in a television series - drama'] = (r'[Bb]est [Aa]ct[oe]r( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*[Dd]rama')

    # best performance by an actor in a television series - comedy or musical
    self.award_dict['best performance by an actor in a television series - comedy or musical'] = (r'[Bb]est [Aa]ct[oe]r( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')
    self.award_dict['best performance by an actor in a television series - musical or comedy'] = (r'[Bb]est [Aa]ct[oe]r( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')

    

    self.film_award['best screenplay - motion picture'] = (r'[Bb]est [Ss]creenplay')

    self.people_award['best director - motion picture'] = (r'[Bb]est [Dd]irector')

    self.people_award['best performance by an actress in a television series - comedy or musical'] = (r'[Bb]est.* [Aa]ctress .*([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')
    self.people_award['best performance by an actress in a television series - musical or comedy'] = (r'[Bb]est.* [Aa]ctress .*([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')

    self.film_award['best foreign language film'] = (r'[Bb]est [Ff]oreign [Ll]anguage [Ff]ilm')
    self.film_award['best motion picture - foreign language'] = (r'[Bb]est.*[Ff]oreign [Ll]anguage')

    self.people_award['best performance by an actor in a supporting role in a motion picture'] = (r'([Aa]ct[oe]r.*[Ss]upporting|[Ss]upporting [Aa]ct[oe]r) (in a|in) [Mm]otion')
    self.people_award['best performance by an actor in a supporting role in any motion picture'] = (r'([Aa]ct[oe]r.*[Ss]upporting|[Ss]upporting [Aa]ct[oe]r) (in any|in|in a) [Mm]otion')

    self.people_award['best performance by an actress in a supporting role in a series, mini-series or motion picture made for television'] = (r'([Ss]upporting.*[Aa]ctress.*[Ss]eries|[Aa]ctress.*[Ss]upporting [Rr]ole.*[Ss]eries)')
    self.people_award['best performance by an actress in a supporting role in a series, limited series or motion picture made for television'] = (r'([Ss]upporting.*[Aa]ctress.*[Ss]eries|[Aa]ctress.*[Ss]upporting [Rr]ole.*[Ss]eries)')

    self.film_award['best motion picture - comedy or musical'] = (r'[Bb]est [Mm]otion [Pp]icture .*([Cc]omedy|[Mm]usical)')
    self.film_award['best motion picture - musical or comedy'] = (r'[Bb]est [Mm]otion [Pp]icture .*([Cc]omedy|[Mm]usical)')

    self.people_award['best performance by an actress in a motion picture - comedy or musical'] = (r'[Bb]est.* [A]ctress [Ii]n [Aa] [Mm]otion [Pp]icture.*([Cc]omedy|[Mm]usical)')
    self.people_award['best performance by an actress in a motion picture - musical or comedy'] = (r'[Bb]est.* [A]ctress [Ii]n [Aa] [Mm]otion [Pp]icture.*([Cc]omedy|[Mm]usical)')

    self.film_award['best mini-series or motion picture made for television'] = (r'[Bb]est [Mm]ini.*[Ss]eries .*[Mm]otion [Pp]icture.*([Tt][Vv]|[Tt]elevision)')

    self.film_award['best original score - motion picture'] = (r'[Bb]est [Oo]riginal [Ss]core.*[Mm]otion [Pp]icture')

    self.people_award['best performance by an actress in a television series - drama'] = (r'[Bb]est.*[Aa]ctress( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*[Dd]rama')

    self.people_award['best performance by an actress in a motion picture - drama'] = (r'[Bb]est.*[Aa]ctress.*[Mm]otion [Pp]icture.*[Dd]rama')

    self.people_award['cecil b. demille award'] = (r'[Cc]ecil.*[Dd]emille')

    self.people_award['best performance by an actor in a motion picture - comedy or musical'] = (r'[Bb]est.* [Aa]ct[oe]r.* [Mm]otion [Pp]icture.*([Cc]omedy|[Mm]usical)')
    self.people_award['best performance by an actor in a motion picture - musical or comedy'] = (r'[Bb]est.* [Aa]ct[oe]r.* [Mm]otion [Pp]icture.*([Cc]omedy|[Mm]usical)')

    self.people_award['best performance by an actor in a supporting role in a series, mini-series or motion picture made for television'] = (r'[Ss]upporting.*[Aa]ct[oe]r.*[Mm]ini')
    self.people_award['best performance by an actor in a supporting role in a series, limited series or motion picture made for television'] = (r'[Ss]upporting.*[Aa]ct[oe]r.*([Mm]ini|[Ll]imited)')

    self.people_award['best performance by an actress in a supporting role in a motion picture'] = (r'([Bb]est|[Ll]eading) ([Ss]upporting [Aa]ctress|[Aa]ctress.*[Ss]upporting).*([Mm]otion [Pp]icture|[Ff]ilm)')
    self.people_award['best performance by an actress in a supporting role in any motion picture'] = (r'([Bb]est|[Ll]eading) ([Ss]upporting [Aa]ctress|[Aa]ctress.*[Ss]upporting).*([Mm]otion [Pp]icture|[Ff]ilm)')

    self.film_award['best motion picture - drama'] = (r'([Bb]est|[Ll]eading) ((([Mm]otion)?\s?[Pp]icture|[Ff]ilm).*[Dd]rama|[Dd]rama.*(([Mm]otion)? [Pp]icture|[Ff]ilm))')

    self.film_award['best television series - drama'] = (r'([Bb]est|[Ll]eading) (([Tt][Vv]|[Ss]eries).*[Dd]rama|([Tt][Vv]|[Ss]eries)|[Dd]rama [Ss]eries)')

    self.people_award['best performance by an actor in a mini-series or motion picture made for television'] = (r'([Bb]est|[Ll]eading) [Aa]ctor.*[Mm]ini')
    self.people_award['best performance by an actor in a limited series or a motion picture made for television'] = (r'([Bb]est|[Ll]eading) [Aa]ctor.*([Mm]ini|[Ll]imited)')


    self.people_award['best performance by an actress in a mini-series or motion picture made for television'] = (r'([Bb]est|[Ll]eading) [Aa]ctress.*[Mm]ini')
    self.people_award['best performance by an actress in a limited series or a motion picture made for television'] = (r'([Bb]est|[Ll]eading) [Aa]ctress.*([Mm]ini|[Ll]imited)')

    self.film_award['best animated feature film'] = (r'[Bb]est [Aa]nimated')
    self.film_award['best motion picture - animated'] = (r'[Bb]est.*[Aa]nimated')

    self.film_award['best original song - motion picture'] = (r'[Bb]est ([Oo]riginal )?[Ss]ong')

    self.people_award['best performance by an actor in a motion picture - drama'] = (r'[Bb]est [Aa]ct[oe]r.*(([Mm]otion)?\s?[Pp]icture|[Ff]ilm).*([Dd]rama)?')
    
    

    self.film_award['best television series - comedy or musical'] = (r'[Bb]est ([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')
    self.film_award['best television series - musical or comedy'] = (r'[Bb]est ([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')

    self.people_award['best performance by an actor in a television series - drama'] = (r'[Bb]est [Aa]ct[oe]r( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*[Dd]rama')

    self.people_award['best performance by an actor in a television series - comedy or musical'] = (r'[Bb]est [Aa]ct[oe]r( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')
    self.people_award['best performance by an actor in a television series - musical or comedy'] = (r'[Bb]est [Aa]ct[oe]r( in a| in)?,? ([Tt][Vv]|[Tt]elevision).*([Cc]omedy|[Mm]usical)')

    

  def getRegex(self, key):
    if key in self.award_dict:
      return self.award_dict[key]
    else: 
      return False

# reg = Regex()
# print(reg.getRegex(' best original score - motion picture '))