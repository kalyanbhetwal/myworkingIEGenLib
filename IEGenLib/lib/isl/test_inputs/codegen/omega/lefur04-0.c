for (int c0 = 0; c0 <= 3; c0 += 1)
  for (int c1 = max(0, 2 * c0 - 3); c1 <= min(c0 + 1, -c0 + 6); c1 += 1)
    for (int c2 = c0; c2 <= min(min(3, 2 * c0 - c1 + 1), c0 + c0 / 2 + 1); c2 += 1)
      for (int c3 = max(max(max(0, c1 - (-c1 + 3) / 3), c0 - (-c2 + 3) / 3), c2 + floord(3 * c1 - c2 - 1, 6)); c3 <= min(3, c0 + c2 / 3 + 1); c3 += 1)
        for (int c5 = max(max(max(max(0, 2 * c3 - 4), c1 - (-c1 + 3) / 3), c2 - (c2 + 3) / 3), c3 - (c3 + 3) / 3); c5 <= min(min(c1 + 1, c3), -c2 + 2 * c3 - (c2 + 3) / 3 + 2); c5 += 1)
          for (int c6 = max(max(max(max(max(-200 * c1 + 400 * c3 - 199, 250 * c3 + 1), 1000 * c0 - 500 * c5 - 501), 667 * c0 - 333 * c1 - (c0 + c1 + 3) / 3 - 332), 333 * c1 + c1 / 3), 333 * c2 + (c2 + 1) / 3); c6 <= min(min(min(min(min(min(1000, 500 * c0 + 499), -200 * c1 + 400 * c3 + 400), 500 * c5 + 501), 1000 * c0 - 500 * c5 + 997), 333 * c2 - (-c2 + 3) / 3 + 333), 333 * c3 - (-c3 + 3) / 3 + 334); c6 += 1)
            for (int c7 = max(max(max(max(500 * c5 + 2, c6), 1000 * c0 - c6), 1000 * c3 - 2 * c6 + 2), 500 * c1 + (c6 + 1) / 2); c7 <= min(min(min(min(500 * c5 + 501, 2 * c6 + 1), 1000 * c0 - c6 + 999), 1000 * c3 - 2 * c6 + 1001), 500 * c1 + (c6 + 1) / 2 + 499); c7 += 1)
              s0(c0, c1, c2, c3, c2 / 3, c5, c6, c7);
