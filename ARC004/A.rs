

fn main() {
    let n = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_end().parse::<i32>().unwrap()
    };
    let mut xy: [[i32; 2]; 100] = [[0; 2]; 100];
    for i in 0..n {
        let (a, b) = {
            let mut s = String::new();
            std::io::stdin().read_line(&mut s).unwrap();
            let mut iter = s.split_whitespace().map(|i| i.parse::<i32>().unwrap());
            (iter.next().unwrap(), iter.next().unwrap())
        };
        xy[i as usize][0] = a;
        xy[i as usize][1] = b;
    }

    let mut max_ans = 0.0_f32;
    for i in 0..n {
        for j in 0..n {
            let distance = ((xy[i as usize][0] as f32 - xy[j as usize][0] as f32).powf(2.0_f32) + (xy[i as usize][1] as f32 - xy[j as usize][1] as f32).powf(2.0_f32)).sqrt();
            if max_ans < distance {
                max_ans = distance;
            }

        }
    }
    println!("{}", max_ans);
}
