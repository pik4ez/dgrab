from actions.abstract_action import AbstractAction


class DiscogsDiscographyAction(AbstractAction):
    def run(self):
        print('discogs:discography:run not implemented')
        # TODO
        # 1. get raw albums list by uri
        # 2. parse albums list using discogs:discography parser
        # 3. for album in albums:
        # 4.     get raw album data by uri
        # 5.     parse data using discogs:album parser
        # 6.     store result in albums list
        # 7. convert result to json
        # 8. print result
        pass
