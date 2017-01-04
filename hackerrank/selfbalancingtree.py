#!/usr/bin/python
'''
Problem:
Hacker Rank - Self balancing tree C++
'''

### TODO ###
/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

void postorder (node * p, int indent=0)
{
    if(p != NULL) {
        if(p->right) {
            postorder(p->right, indent+4);
        }
        if (indent) {
            cout << setw(indent) << ' ';
        }
        if (p->right) cout<<" /\n" << setw(indent) << ' ';
        cout<< p->val << " " << p->ht << "\n ";
        if(p->left) {
            cout << setw(indent) << ' ' <<" \\\n";
            postorder(p->left, indent+4);
        }
    }
}

node * add(node * n, int val)
{
    if (n == nullptr) {
        node * new_node = (node*)malloc(sizeof(node));
        new_node->val = val;
        return new_node;
    } else if (val < n->val) {
        n->left = add(n->left, val);
        n->ht = n->left->ht + 1;
    } else if (n->val < val) {
        n->right = add(n->right, val);
        n->ht = n->right->ht + 1;
    }

    return n;
}

int get_balance(node * left, node * right) {
    if (left != nullptr && right != nullptr) {
        return left->ht - right->ht;
    } else if (left != nullptr) {
        return left->ht + 1;
    } else if (right != nullptr) {
        return (-1 * right->ht) - 1;
    } else {
        return 0;
    }
}

node * rotate_left(node * pivot);
node * rotate_right(node * pivot);

node * rotate_left(node * pivot) {
    node * rotator = pivot->right;
    
    if (rotator->left != nullptr && rotator->right != nullptr) {
        if (rotator->right->ht < rotator->left->ht) {
            rotator = rotate_right(rotator);
        }
    } else if (rotator->left != nullptr) {
        rotator = rotate_right(rotator);
    }
    
    node * inside = rotator->left;
    pivot->right = inside;
    pivot->ht -= 2;
    rotator->left = pivot;
    
    if (pivot->ht < 0) {
        pivot->ht += 1;
        rotator->ht += 1;
    }
    return rotator;
}

node * rotate_right(node * pivot) {
    node * rotator = pivot->left;
    
    if (rotator->left != nullptr && rotator->right != nullptr) {
        if (rotator->left->ht < rotator->right->ht) {
            rotator = rotate_left(rotator);
        }
    } else if (rotator->right != nullptr) {
        rotator = rotate_left(rotator);
    }
    
    node * inside = rotator->right;
    pivot->left = inside;
    pivot->ht -= 2;
    rotator->right = pivot;
    
    if (pivot->ht < 0) {
        pivot->ht += 1;
        rotator->ht += 1;
    }
    return rotator;
}

node * rotate_tree(node * n, bool imbal, int val) {
    int balance = get_balance(n->left, n->right);
    node * r;
    
    // Recurse right if right bigger than left
    if (balance < -1) {
        r = rotate_tree(n->right, true, val);
        
        // r is rotator, n is pivot
        if (r == nullptr) {
            return rotate_left(n);
        } else {
            n->right = r;
            return n;
        }
    } 
    // Recurse left if left bigger than right 
    else if (1 < balance) {
        r = rotate_tree(n->left, true, val);
        
        // r is rotator, n is pivot
        if (r == nullptr) {
            return rotate_right(n);
        } else {
            n->left = r;
            return n;
        }
    } 
    // Return null if rotator point found
    else {
        if (!imbal) {
            if (val < n->val && n->left != nullptr) {
                n->left = rotate_tree(n->left, false, val);
            } else if (val > n->val && n->right != nullptr) {
                n->right = rotate_tree(n->right, false, val);
            } 
            
            return n;
        } else {
            return nullptr;    
        }
    }
}

node * insert(node * root,int val)
{
    root = add(root, val);
    //postorder(root);
    //cout << "\n\n\n";
    root = rotate_tree(root, false, val);
    //postorder(root);
    root = add(root, val);
    return root;
}

//input
//    3
//  /  \
// 2    4
//       \
//        5
        
// output
//     3
//  /  \
// 2    5
//     / \
//    4   6
