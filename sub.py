import dns.resolver
import threading 


sub_domains  = open('subs.txt','r').read().splitlines()

def find_sub(domain):
    for subdomain in sub_domains:
        dom = subdomain + "." + domain
        try:
            answers = dns.resolver.query(dom, 'A')
            for rdata in answers:
                if rdata:
                    print dom
        except Exception:
            pass


def main(): 
    threads = []
    for i in range(20):
        t = threading.Thread(target=find_sub, args=(find_sub("vg.no")))
        threads.append(t)
        t.start()
     

if __name__ == '__main__': 
     main()
