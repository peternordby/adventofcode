import math
import time
from heapq import heapify, heappop, heappush

from PIL import Image

input = '''2522414939711849132228579816748823728379124311418111161529639822623219297197656312386831265718721211
7119125991574111336131978938112955121422183362398517132564814661292561181421134141499624511692694112
3127235291311117732711221595212461287834821864268181236173834391241692536216841911355119911169521283
1181155152189111774111156796369418892573474529449114243368393188187466226115613499124591912775811129
4511586224241188433132151131912322433627252532818342691614969559425683161447111791121549111146484532
5413831212391138911819213166957149213922161137291919117113531382416132121124858321148398497135261112
3141189114547157882263926111828665483177711211394322187226895913495654276512911298585113827786152821
8139154185512648535373192171842522111781272122639619926142743623114419711811419181134834173248346866
6131817237181957336623411991444413536213224516221697817415389416311235139732243655118584442412599145
1718527358218195924512318645311122933297111329286687374945374614773121499269961183811521727398185311
3481151521221189311126811235832569921337354392175131599321326783387163848295333231182825314233581171
5171429946536911171547532412699913195693631981517211295814192796223191999671726151521111228699694495
5731624261487716916211124279184347912542257442518826222117821961594127731715739323835513111141439813
1369513736556212936295111719858412198182886373247978725451813524111444118681111124821121862374272185
3312732241492183466791771757118623969963121992111428649113794614499532441441141428121976111121223453
1323512461571182817929939121211713121331191618931184488921591924371235949236168615391825511262223251
1844736754225215827118148196139158162168679832813293479114597571111121411671116786889524639436242557
4129283884611621139311619918595314638141219118197141982129117931591223136764173918143299992113253194
6671213763912343811231319922512514312369111929282929165115129559956116288484182461615162311121211148
2181433993113222146117211167911285371166791149379422215815118977498295214751775791959491311282321124
1893917971839118469544291628117512951141192191241581996647811817614684113124339455132319119114111833
3194199213412152114124178931454213517429615776219211422169278113182121444219111131179993118914924997
8219157811341224982161348148111137699341495216731165567471616617941931189972413946971741111281539372
3152991117932991922251181118416182931569516111612171922275213185896565291135832617881969216831717171
8121312176196962611113271281983885941434758534152637122112688674391761284711462212621329281482136967
8912131712629191413717199581682992241791258247943427519627115113181185118893474742221612199416241114
2221161716133212262324458823185719629698212514616894944235615445525451113712232992549892442332219993
6911428166248291364296657112178221953148681417139715698913134796992291191172362729179523142135611926
9193236341295518167899946545124351411258968629291352811613236111815329611335145489738414432321321432
6499112739337254948563116237193161125349119739111891452711618219882237913445111154917766361994516299
4229111836211397937422211492241292322326927188315516321228751111732223381939852566191913828113619658
4833174199812161182295513144544918898488232695919771112444311825381832117171263412399721619352658112
7345157387254272529181221134266152214182213139812959885519442556151428591127252113184465879292314161
4121465311125417865689227119793711491911121482117238853817572153785844421215789241437331227838558423
7523449997166932491931658961611531315911811164945424124681119911514197115371331269117411119195916939
9128356914695294253146521193138399121128911413417518232932311581117299227259128821183119275215162333
8227711221398832121511812135311996274919173171129616622917349424125661165191393153231221123245228595
4661116386124142435676668639172615623882971851132123111533289551472765422233434392326129112321811177
1114217118682227172769681833229791919152755377579244542792389334115282624447734191114139324262441812
6333952614971166184221548154711268114116731892434448374621261433111364575261971518211189121489159114
2643196276215391358127393286244464171242921198641798351383314226421425913793645897272129967531283212
5221131154713291512567291442563229223436517211423727422223922197775199547432692311674116717814141189
1819812131622311541323862952123752381291168856181384249979548263219194576715373571921367953197516599
2698391452599945182154313714292112611651861235644938114519912171341121343514175192421245367422118845
1611517822616311553312232428414211183613187966271813393742419936965141554638677392552594157325161112
2616289141825669321758111712577299113571118732335179737221439878266941941412314591611896381134423452
1527518133297694711977121278995238611939331141152651419529812614622461553336429953291144879147151561
6213921184159959912652486789753618112941772164917131997527427312889291111154689437932652465371922993
1589621196261511215112194551558331982928756286156353223919126143241698114592611956762736234771235113
8165134892151911811992165572238498525759113712471968163566177711133512677122986191491333635131511791
5121221111325162242111121122831421669143125569751141468542973371346331562315313969174126843799229968
9311826253374818154286131873371269258326126213915219114431182511695131248953693559426228911488261322
6591912229221199191129116241691328113778565819111151417179291232116973821215214994781183977822113919
2655733341912396361634999147955152969525556354836191314176963932513419228391962945211314943311783881
3118513322278916893854417223419174791345313746443425946927242923322912213948211723553112339311144122
5393914115613713593912123214127131162129218517429461299451985249947485233933233921659915294223287391
1136191983199344171731412199186927561119191219449214216992974151651232175255264491687372483691287841
9979467192332442137813919617268197123213515265393883398799246483166214491885851268864128943317146789
5137813992711119791889189943164114839536152943452515191991159113143114778121351814419428981641345112
1139549732431283823889222929962191941833515674999331261216489474223871213121931162521316251539111719
9648979341691798386938175539169825511368121122518621349181719251191923915224299327193775463296152619
2311686178629622129357219123853166497242116415121621253426142621912642623299254411219291611241129171
7121116711145236394141163917421425189867111859681243149523155243991912931714194994881892515611113358
1818136725482517518915422141595131218142168351111612261359827276317281438261183179221111193792271938
1139232197366129111613197151415986632374322119127213743117112134123523163898634321495279921127151221
1455314773112765478191612311924292793128399375128619158595924411116981162347622141987917914911132244
8251232313319753992222152996483791494285141669117359623333132226419358827367424225513193954688331113
6111234734513789142262268362695121242113336193619579246538959597918449963359798412951815198197838189
1578813352693398121218392393228426881375119641573137139414326439413217641415223545191618221945511142
1911342279476333131545622131253816127514398158171126197453819142121921259134342249152113279914226717
1181629961152116111141119143162937219335744191534119193429336859258124131916718881314941225494635341
3222424734834755922262268951935198255226535129825126496551953155492124112112211175279241996463213119
1593211411152338281162891684932212324129938521214175966519115616258481414912622151114391841157816911
9141742471551231591911521557311235228349158433361181732488334569224298416181419199789621481599971133
6431198331792522412624936255227425156144247631813877119181883195211392367931313972411512151112618967
2267991391137261324361516124912921857412152165751315973914128819334272982513357434496931189261186356
9731813991313183129492113339525281972169411596682712297561568989281898122432796821932939271461411118
9527134412189191252414927113351112113969912114126318294265393127727772965192682248351121436671131949
2934611311112198347953125482617172423953569149249533769821945569113994113763296118552242729222291678
1119821798911229468135239194762377711532847158111932619121161511191149211189681391816252112113662712
6214121139114981831641312844617298831755199745993362226745938625473922122411831659139316811819252196
3924199495311615731298928326511113989189152121371528721212116121162831153589349432417428485259451119
5671887941514276146115224125348154943341717912911297112361317998423125793133517712118312219932327921
3441237411174773198815869762621122911338922117263951832219575348184521221829897832142581331278543895
2211991891331676514418141258839222191162231674139112521311364936142331963939355929771951341931514622
3747831369635231342124231137812472365447171343913391192962128751842928364413553211815321439116297947
3831431319439189562841352632121129765521147556153119234918143471929436282139114141121119611153125122
2139868123226218473119733131211449463783356211861164441899319364198832981181141122831449381518499837
4838641963928213442551872111262529681463281171145974513318477114933139791111182125546543252119792122
1959561559542891384239921218331871441193122413948521139911152336487323225262262552411443442912132194
4314213327111115624539372751956191844329316172123933514157637524332315229214279183693125891951974216
4121185311217111892962855325351544592933191142755325176455121327454442754548131832152935917115212312
1154235973614813121713111278736277174981611157831121152921813123844315723944435135596869139295122111
1191164343178491732236111338376338452883881999141122152922792155423112322571421418882716619274477923
2942191994588631294975973591371724121221115633251176816331419716599528162253122115638991142695511897
1515552919629173654117969541842691298189369498352573484463845716711425113318121951513141136111791614
2338151152352731719473221793641322611375192411551164617517155997347919611627517828225538711524251539
9161345711264179182921881491169952213815926531391622324113233224122432611247811369169532962163481152
1396729196339538914672129619583981562917642411114972418153771391277221143911393951111126922719818115
8795124512286141121694662341622161368222432113312766132151575916676412414382618623933742751114159519'''

test = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''

cave = input.split('\n')
cave_map = []
for i in range(5):
    for row in cave:
        cave_row = []
        for j in range(5):
            for num in row:
                num = int(num) + i + j
                if num > 9:
                    num -= 9
                cave_row.append(num)
        cave_map.append(cave_row)


class Node():
    # Initiates a new node with xy position and cost to travel across (-1 is blocked)
    def __init__(self, x, y, cost):
        self.g_cost = math.inf
        self.h_cost = 0
        self.f_cost = self.h_cost + self.g_cost
        self.cost = cost
        self.parent = None
        self.pos = [x, y]
        self.x = x
        self.y = y

    # Comparative methods
    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def __le__(self, other):
        return self.f_cost <= other.f_cost

    def __eq__(self, other):
        return self.pos == other.pos

    def __gt__(self, other):
        return self.f_cost > other.f_cost

    def __ge__(self, other):
        return self.f_cost >= other.f_cost

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_blocked(self):
        return self.cost == -1

    def get_g_cost(self):
        return self.g_cost

    def get_h_cost(self):
        return self.h_cost

    def get_f_cost(self):
        return self.f_cost

    def get_cost(self):
        return self.cost

    def set_g_cost(self, g):
        self.g_cost = g
        self.f_cost = g + self.get_h_cost()

    def set_h_cost(self, h):
        self.h_cost = h
        self.f_cost = h + self.get_g_cost()

    def set_parent(self, node):
        self.parent = node

    def get_parent(self):
        return self.parent

# Grid class to create node representation, getting neighbour nodes and printing the maps


class Grid():
    def __init__(self, map, start, goal):
        self.width = len(map[0])
        self.height = len(map)
        self.grid = map
        self.start = start
        self.goal = goal
        self.nodes = []
        self.create_node_grid()
        self.str_grid = []

    # creates a grid consisting of nodes representing the map
    def create_node_grid(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                node = Node(x, y, self.grid[y][x])
                row.append(node)
            self.nodes.append(row)

    # returns the unblocked nodes north, west, east and south of the current node
    def get_neighbours(self, node):
        neighbours = []
        moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        for move in moves:
            pos_x, pos_y = node.get_x() + move[0], node.get_y() + move[1]
            if pos_x >= 0 and pos_x < self.width and pos_y >= 0 and pos_y < self.height:
                neighbour = self.nodes[pos_y][pos_x]
                neighbours.append(neighbour)
        return neighbours

    # calculate the euclidean distance between two nodes
    def dist(self, a, b):
        w = abs(a.get_x() - b.get_x())
        h = abs(a.get_y() - b.get_y())
        return min(w, h)*(1.4) + abs(w-h)

    # creates a PNG image of the map with the path from start node to goal node
    def print_image(self, path, scale=10):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if self.start.get_x() == x and self.start.get_y() == y:
                    row.append("S")
                elif self.goal.get_x() == x and self.goal.get_y() == y:
                    row.append("G")
                elif [x, y] in path:
                    row.append("O")
                else:
                    row.append('#')
            self.str_grid.append(row)

        # Create an all-yellow image
        image = Image.new('RGB', (self.width * scale, self.height * scale),
                          (255, 255, 0))
        # Load image
        pixels = image.load()

        # Define what colors to give to different values of the string map (undefined values will remain yellow, this is
        # how the yellow path is painted)
        colors = {
            '#': (211, 33, 45),
            'S': (255, 0, 255),
            'G': (0, 128, 255)
        }
        # Go through image and set pixel color for every position
        for y in range(self.height):
            for x in range(self.width):
                if self.str_grid[y][x] not in colors:
                    continue
                for i in range(scale):
                    for j in range(scale):
                        pixels[x * scale + i,
                               y * scale + j] = colors[self.str_grid[y][x]]
        # Show image
        image.show()


# Class for running and initializing the A* path finding algorithm
# The algorithm is implemented with inspiration from Sebastian Lague's youtube series
# Source: https://www.youtube.com/watch?v=-L-WgKMFuhE&t=257s&ab_channel=SebastianLague
# It is modified according to the task
class A_Star():
    # Initializing the datastructures needed for the algorithm to work
    def __init__(self, start_node, goal_node, grid, h, w):
        self.start_node = start_node
        self.goal_node = goal_node
        self.grid = grid
        self.open = []
        heapify(self.open)
        self.closed = []
        self.start_node.set_h_cost(
            self.grid.dist(self.start_node, self.goal_node))
        self.start_node.set_g_cost(0)
        self.visited = [[0 for _ in range(h)]
                        for _ in range(w)]

    # Function for finding the most cost efficient path fram start node to goal node
    def find_path(self):
        # Add start node to min heap
        heappush(self.open, self.start_node)

        # Loop until path is found
        while True:
            # Set current node to node with lowest f_cost in min heap
            current = heappop(self.open)
            self.closed.append(current)
            self.visited[current.get_y()][current.get_x()] = 1

            # return path to goal node if the path is found
            if current == self.goal_node:
                path = []
                node = current
                while node is not None:
                    path.append(node.pos)
                    node = node.get_parent()
                return path[::-1]

            # get neighbour nodes of current node and calculate g_cost and h_cost of non-blocked nodes
            neighbours = self.grid.get_neighbours(current)
            for node in neighbours:
                if self.visited[node.get_y()][node.get_x()]:
                    continue

                node.set_h_cost(self.grid.dist(node, self.goal_node))

                if ((current.get_g_cost() + node.get_cost()) < node.get_g_cost()) or node not in self.open:
                    # if node not in self.open:
                    node.set_g_cost(current.get_g_cost() + node.get_cost())
                    node.set_parent(current)
                    # if node is not explored yet, add it to min heap
                    if node not in self.open:
                        heappush(self.open, node)


def run_task(task):
    int_map = task

    h, w = len(int_map), len(int_map[0])

    start_y, start_x = 0, 0
    goal_y, goal_x = h-1, w-1

    start = Node(start_x, start_y, int_map[0][0])
    goal = Node(goal_x, goal_y, int_map[h-1][w-1])

    grid = Grid(int_map, start, goal)

    a_star = A_Star(start, goal, grid, h, w)
    path = a_star.find_path()
    print("\n\nPath for task out of cave" + "\n\n")
    risk = 0
    for pos in path:
        risk += int_map[pos[1]][pos[0]]
    risk -= int_map[0][0]
    print('Total risk is', risk)
    grid.print_image(path)


def main():
    print("Starting")
    start = time.time()
    run_task(cave_map)
    print(time.time() - start, 'seconds to run')
    # run_task(2)

    # run_task(3)

    # run_task(4)


main()