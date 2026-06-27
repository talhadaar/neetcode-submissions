pub struct Codec {}

impl Codec {
    fn new() -> Self {
        Codec {}
    }

    fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {
        let mut out = Vec::new();
        let mut queue = std::collections::VecDeque::new();

        if let Some(node) = root {
            queue.push_back(Some(node));
        } else {
            return "#".to_string();
        }

        while let Some(maybe_node) = queue.pop_front() {
            if let Some(node) = maybe_node {
                out.push(node.borrow().val.to_string());
                queue.push_back(node.borrow().left.clone());
                queue.push_back(node.borrow().right.clone());
            } else {
                out.push("#".to_string());
            }
        }
        out.join(",")
    }

    fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
        let tokens = data.split(',').collect::<Vec<_>>();

        if tokens.is_empty() || tokens[0] == "#" {
            return None;
        }

        let root = Rc::new(RefCell::new(TreeNode::new(tokens[0].parse().unwrap())));
        let mut queue = std::collections::VecDeque::new();
        queue.push_back(root.clone());

        let mut i = 1;
        while i < tokens.len() && !queue.is_empty() {
            let node = queue.pop_front().unwrap();

            if i < tokens.len() && tokens[i] != "#" {
                let left = Rc::new(RefCell::new(TreeNode::new(tokens[i].parse().unwrap())));
                node.borrow_mut().left = Some(left.clone());
                queue.push_back(left);
            }
            i += 1;

            if i < tokens.len() && tokens[i] != "#" {
                let right = Rc::new(RefCell::new(TreeNode::new(tokens[i].parse().unwrap())));
                node.borrow_mut().right = Some(right.clone());
                queue.push_back(right);
            }
            i += 1;
        }

        return Some(root);
    }   
}