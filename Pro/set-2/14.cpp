#include<bits/stdc++.h>
using namespace std;

class SegmentTree{
	int *tree, n;
public:
	SegmentTree(int n=100000){
		tree = new int[2*n];
	}
	void buildTree(vector<int> vec) {
	    this->n = vec.size();
		for (int i=0; i<vec.size(); i++)
			tree[n+i] = vec[i];
		for (int i=n-1; i>0; --i)
			tree[i] = tree[i<<1] ^ tree[i<<1 | 1];
	}
	void updateTreeNode(int p, int value) {
		tree[p+n] = value;
		p = p+n;
		for (int i=p; i>1; i>>=1)
			tree[i>>1] = (tree[i] ^ tree[i^1]);
	}
	int sum(int l, int r){
		int res = tree[n+r];
		for(l+=n, r+=n; l<r; l>>=1, r>>=1) {
			if(l&1)
				res = (res ^ tree[l++]);
			if (r&1)
				res = (res ^ tree[--r]);
		}
		return res;
	}
};

int main(){
	int n, queries, l, r;
	cin>>n>>queries;

	vector<int> vec(n);
	for(int i=0; i<n; i++)
		cin>>vec[i];

	SegmentTree tree;
	tree.buildTree(vec);
	for(int i=0; i<queries; i++){
        cin>>l>>r;
        l--;
        r--;
        cout<<tree.sum(l,r)<<endl;
	}
	return 0;
}
