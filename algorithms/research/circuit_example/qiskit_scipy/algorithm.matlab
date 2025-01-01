% Algorithm(1)
objective1 = @(w) -u'*w + q*sqrt(w'*w);
constraint1 = @(w) deal([], sum(w) - 1);
constraint2 = @(w) deal([], w - w_bar - zeta);

options = optimoptions('fmincon', 'Algorithm', 'interior-point');
w0 = ones(3, 1) / 3;
[u, q, w_bar, zeta] = deal([1; 2; 3], 1, [0.5; 0.5; 0.5], 0.1);
[w1, fval1] = fmincon(objective1, w0, [], [], [], [], [], [], @(w) deal([], [constraint1(w); constraint2(w)]), options);
disp('Algorithm(1) result:'), disp(w1)

% Algorithm(2)
objective2 = @(w) w'*w;
constraint3 = @(w) deal([], u'*w - r_min);

r_min = 1;
[w2, fval2] = fmincon(objective2, w0, [], [], [], [], [], [], @(w) deal([], [constraint1(w); constraint3(w)]), options);
disp('Algorithm(2) result:'), disp(w2)

% Algorithm(3)
objective3 = @(x) [-u; q]' * [x(1:end-1); x(end)];
constraint4 = @(x) deal([], sqrt(sum(x(1:end-1).^2)) - x(end));

x0 = ones(4, 1);
[x3, fval3] = fmincon(objective3, x0, [], [], [], [], [], [], @(x) deal([], [constraint1(x(1:end-1)); constraint4(x)]), options);
disp('Algorithm(3) result:'), disp(x3)
