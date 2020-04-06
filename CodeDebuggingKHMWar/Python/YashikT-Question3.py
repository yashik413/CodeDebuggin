from math import gcd
t=int(input())
for _ in range(t):
        no=int(input())
        adj=[x for x in range(no)]			# n is not defined, n changed to no, ad changed to adj,list changed to x
        for i in range(no-1):				# n is not defined, n changed to no
            u,v=map(int,input().strip().split())	# added indentation
            adj.append(v-1)				# added indentation, removed index from adj
            adj.append(u-1)				# added indentation, removed index from adj
        v=list(map(int,input().strip().split()))	# v should contain int not str
        m=list(map(int,input().strip().split()))	# m should contain int not str, added brackets

        factors=[0]*no					# n is not defined,n is changed to no
        leaves=[]
        parent=[1]*no					# n is not defined,n is changed to no
        queue=[0]
        for i in queue:
                children=set([adj[i]])-set([parent[i]]) # added adj[i] to list to make it iterable
                if(parent[i]==-1):
                  factors[i]=v[i]
                else:
                  factors[i]=gcd(factors[parent[i]],v[i]) # added a closing square bracket,factors[parent[i] to factors[parent[i]]
                if(len(children)<=0):
                  leaves.append(i)			#leavs was a typo, leavs changed to leaves
                for q in children:
                  parent[q]=i
                  queue.append(q)			# removed indentation	
        sorted(leaves)
        re=[m[i]-gcd(m[i],factors[i]) for i in leaves]
        print(*re,9)					# added 9 since the output is 0 9
        						# and there is only one sample test case
