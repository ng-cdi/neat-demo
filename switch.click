
fd0 :: FromDevice(0);
fd1 :: FromDevice(1);
fd2 :: FromDevice(2);

td0 :: ToDevice(0);
td1 :: ToDevice(1);
td2 :: ToDevice(2);

q0 :: Queue(1024) -> td0;
q1 :: Queue(1024) -> td1;
q2 :: Queue(1024) -> td2;

in_supp0, out_supp0 :: Suppressor;
in_supp1, out_supp1 :: Suppressor;
in_supp2, out_supp2 :: Suppressor;

switch :: EtherSwitch();

fd0 -> Print('IN0') -> in_supp0 -> [0]switch;
switch[0] -> out_supp0 -> q0;

fd1 -> Print('IN1') -> in_supp1 -> [1]switch;
switch[1] -> out_supp1 -> q0;

fd2 -> Print('IN2') -> in_supp2 -> [2]switch;
switch[2] -> out_supp2 -> q0;
