import bottle
import os


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff12',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/move')

def decide ():
        # where is head and where is food
        for snake in snakes:
            if snake.id == "2fd899c5-b1cc-41ae-a4c4-782a9fe168a6" :
                break
        
        
        mysnake = snake
        head = snake.coords[0]
        headx = head[0]
        heady = head[1]
        
        firstfood = food[0]
        foodx = firstfood[0]
        foody = firstfood[1]
        
        if  heady != foody  :
                if  heady > foody :
                    return "north"
                if  heady < foody :
                    return "south"
                
        
        
        if headx > foodx :
            return "west" 
        if  headx < foodx :
            return "east"
        

            
    

def move():
    data = bottle.request.json

   

    return {
        'move': decide(),
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
