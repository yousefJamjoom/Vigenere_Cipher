alpha = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
frequency = [16,3,6,8,26,4,3,12,13,1,1,7,6,14,16,4,0.5,13,12,18,6,2,3,1,4,0.5]

def shift(word, n):
    Sum = 0
    newWord = (" "*n)+word
    for i in range(len(word)):
        if word[i] == newWord[i]:
            Sum +=1
    return Sum


def pattern(List, n):
    count = 0    
    Sum = 0
    for i in range(len(List)):
        if ((i+1)%n) == 0:
            Sum += List[i]
            count += 1
    if count == 0:
        return (Sum,0)
    return ((Sum/count),count)
            
            
def maxPattern(List):
    Sum = []
    index = 0
    Count = []
    for i in range(50):
        sum1, count1 = pattern(List, i+1)
        Sum.append([i+1,sum1])
        Count.append(count1)
        print("####### index:",i+1)
        print("####### -------------->Sum:",sum1)
        print("####### count:", count1)
        
    Sum.sort(key = lambda x: x[1], reverse=True)
    bestFive = Sum[0:5]
    bestFactor = 0
    bestIndex = 0
    for i in bestFive:
         factor = 0
         for e in bestFive:
             if (e[0]%i[0]) == 0:
                 factor +=1
         if factor > bestFactor:
             bestFactor = factor
             bestIndex = i[0]
             
             
    print("bestFive:",bestFive)
    print("bestIndex:",bestIndex)
    return bestIndex
        

def maxShift(word):
    x = 0
    List = []
    for i in range(len(word)):
        x = shift(word, i+1)
        print("iter:", i+1)
        print("-------->sum:", x)
        List.append(x)
    
    index = maxPattern(List)
    print("index is equal to:", index)
    return index ## ===================================> length of the key

def groupby(word, index):
    print("index:", index)
    List= []
    newWord = ""
    for i in word:
        newWord += i
        if len(newWord) == index:
            List.append(newWord)
            newWord = ""
    return List

def recursionList(List):
    if len(List) == 1:
        return List
    else:
        powerList = []
        for i in range(len(List)):
            if i == 0:
              newList = List
            elif i != 0:
                newList = [List[i]]+List[0:i]+List[i+1:len(List)]
            elif i == len(List)-1:
                newList = List[-1]+List[0:len(List)-1]
            recResult = recursionList(newList[1:len(List)])
            for v in recResult:
                powerList.append(newList[0]+v)
        return powerList           

def findNum(char):
    for i in range(len(alpha)):
        if alpha[i] == char:
            return i

def maxCalc(CharList):
    AllSum = 0
    AllComb = recursionList(CharList)
    maxShift = 0
    for i in AllComb:
        maxSum = 26
        shift = (findNum(i[0])-4)%26
        for e in i[1:len(i)]:
            maxSum += frequency[((findNum(e)-shift))%26]
        if maxSum > AllSum:
            AllSum = maxSum
            newChar = i
            maxShift = shift
    print("Shift:",maxShift)
    return maxShift

def matchNth(List, n):
    char = []
    sumChar = []
    check = False
    for i in List:
        for e in range(len(char)):
            if char[e] == i[n]:
                sumChar[e] += 1
                check = True
        if check == False:
            char.append(i[n])
            sumChar.append(1)
        check = False
        
    print()
    print("nth:",n+1)
    print("Length:", len(List))
    print("Char:",char)
    print("sumChar:",sumChar)
    
    CharList = []
    for e in range(9): ## =============================> depth
        for i in range(len(sumChar)):
            if sumChar[i] == max(sumChar):
                CharList.append(char[i])
                char.pop(i)
                sumChar.pop(i)
                break
    
    print("Max Six:", CharList)
            
    return maxCalc(CharList)
        
def getOriginal(char, shift):
    index = 0
    for i in range(len(alpha)):
        if alpha[i] == char:
            index = i
    return alpha[(index-shift)%26]
        
def getAllMatches(word):
    index = maxShift(word)
    List = groupby(word, index)
    shiftList1 = []
    for i in range(len(List[0])):
        shiftList1.append(matchNth(List, i))
    
    print("All Shifts:", shiftList1)
    

    sentence = ""
    newWord = ""
    for e in List:
        for i in range(len(e)):
            newWord += getOriginal(e[i], shiftList1[i])

        sentence += newWord
        newWord = ""
    print(sentence)
    key = ""
    for i in shiftList1:
        key += alpha[i]
    return key


def getShift(char):
    for i in range(len(alpha)):
        if alpha[i] == char:
            return i

def CeaserCipher(text, shift):
    newText = ""
    for i in text:
        newText += alpha[getShift(i)+shift]
    return newText

### examples to decode
word1 = "EUHRXRGKIPQYZFHSULHPEAGZMAWWXXOHGBOIAAHGTWFDVLHSZBQIEIBSPRVSLVVWDPIHXUGTWYLXXGNOFNPHAJKMRLUDZRESVAHGIIQWLROAQGKECSGKIECRLGREHWHPINOSVTWLTTBZIEUSNGKITEEWLGJIARSEGEGHEAFIYHDPHXNWMBPXWJKMRLGKIYCAABIRPXHUINPHWSQEIYEHWTQHMAWMIPRWLROELRFICXEHWCGGBGRXWIBSMAKSVFRJBEANMAFVMDXMGIFWLNVXPRBWWSHOHQGGTNUIILRFEHUIAJKMRLVPTRNXPRPXDXUHWRREZNWMDR"
word2 = "VVHQWVVRHMUSGJGTHKIHTSSEJCHLSFCBGVWCRLRYQTFSVGAHWKCUHWAUGLQHNSLRLJSHBLTSPISPRDXLJSVEEGHLQWKASSKUWEPWQTWVSPGOELKCQYFNSVWLJSNIQKGNRGYBWLWGOVIOKHKAZKQKXZGYHCECMEIUJOQKWFWVEFQHKIJRCLRLKBIENQFRJLJSDHGRHLSFQTWLAUQRHWDMWLGUSGIKKFLRYVCWVSPGPMLKASSJVOQXEGGVEYGGZMLJCXXLJSVPAIVWIKVRDRYGFRJLJSLVEGGVEYGGEIAPUUISFPBTGNWWMUCZRVTWGLRWUGUMNCZVILE"
word3 = "EFMZRNQMWOBEBUIXDDMTRDGAXGJUBKNEIVWATHLHJDZUOAOENVIBROCXCSLZUIFUDCSPHSGMDTQTQAUNVSWTVOAKXUPZVNGATAQJQLRVGSIYROSMWSJUBKGATAITHFNVIIZKEOSMWSJUBKUTHWVIYUQXSHPKBNVHCOBSLRRJJSAZFOLHJFMRVKRPDKBNVSOHDYKUZEFPXHPGAOABDBMBRNVYNCCJBNGIPFBOPUYTGZGRVKRHCWWTFIZLJFMEBUPTCOXVEEPBPHMZUEYHVWAZVCFHUGPOCPVGVOVEFOEMDTXXBDHVTRQYPRRXIZGOASVWTCNGAAYETUMJCRBZGOUSVNTFPBCGY"
word4 = "SOMZAQLLIWSZKBBOGKLBBQJNNVODSKIPVSSQWUIDLGWTBTALGPVSHPETIDAJUVNULYOHVMJRBVZYALWUIQKRDLBUUQAUAQLFAJPUWDCVIXGDIFEAJIWZIZWBQJIFGPWULMMRDVZUKRKOMXHNAVXXWJAHZZZMSAWIJGPLJQSSPPNGDNNVODSKOTGRWCHPVSAQPOIFOFAUEQHPAWIDWYLYWSJYIAPQWVLLZUWLYLKMFZAQCELJERMOGKLVAUFELVMFJWKYUGKGYZWYWNNVODSKOHZQWJANIZLQKTMMJCAEYGAQEAMEGKAHZQKNWYSXALCTGODYETQELFWAQFAQLVAEAZHLBAOPEAMSJYJKXDGENHUEFMXSMBJMCYIYKRNBTKEYCUQRAAAUBAFCOJWYHSPLZBJMCYIYEGJNQESLWYBNWAWBAQARWWXXACOHKOMKQSIFWBGUWIDCZNMFGRDLEAJJZIMOSSOLQFJCMBQDWQORQXDYJKQZYCJBQFQYJKMEHCYPIXDWXLKMMQAPBBJMZBKQKMXQMOLQKMJQSSPFXDGENHUYWPODPAKSXJWZKAEVCEDWRPMILFATAQDTAZIESPPPAFKUESTQFHKFETSRPOMKVMWULIAJHKWULZAABQJ"
word5 = "WiqikmstqckliqstmhmviYmugkmwtbiquhisckdsmdmECnuhhrmjjetjiktswbctEjtbekgeklmnYmuwmuhdktlittbesnqmjckymtbiqluyEfustwckkctihhymubmwEjniiheklLmttcjcgiymuukdiqstckdKiviqlmkkcleviymuuoKiviqlmkkchitymudmwkKiviqlmkkcqukcqmukdckddisiqtymuKiviqlmkkcjcgiymurqyKiviqlmkkcscylmmdayiKiviqlmkkctihhcheickdbuqtymu"
word6 = "BTUVEFOUJOTBVEJVOJWFSTJUZJXJMMDIBOHFUIFXPSME"
word7 = "FAMEEQEEQRRQOFUHQXKFTQEQOGDUFKZQQPEARMZADSMZULMFUAZMZPFAQHMXGMFQMZPOTAAEQHMDUAGEEQOGDUFKBDAPGOFEMZPBAXUOUQEFTQYMZMSQDDQEBAZEUNXQRADEQOGDUFKZQQPEEAYQEKEFQYMFUOIMKARPQRUZUZSFTQDQCGUDQYQZFERADEQOGDUFKMZPOTMDMOFQDULUZSFTQMBBDAMOTQEFAEMFUERKUZSFTAEQDQCGUDQYQZEFTUEUEPURRUOGXFQZAGSTUZMOQZFDMXULQPPMFMBDAOQEEUZSQZHUDAZYQZFIUFTFTQGEQARXAOMXMZPIUPQMDQMZQFIADWEFTQBDANXQYEMDQOAYBAGZPQP"

