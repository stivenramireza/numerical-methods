 @RequiresApi(api = Build.VERSION_CODES.M)
    public void incrementalSearchMethod(Double x0, Double delta, int ite) {
        graph.removeAllSeries();
        function.setPrecision(100);
        for (int i = 0; i < ite; i++) {
            TableRow fila = new TableRow(getContext());
            fila.setId(100+i);
            TextView vXn = new TextView(getContext());
            vXn.setId(200+i);
            String initial = String.valueOf(x0);
            vXn.setText("     "+ initial + "           ");
            TextView iters = new TextView(getContext());
            iters.setId(300+i);
            iters.setText("     "+String.valueOf(0) + "           ");
            TextView func = new TextView(getContext());
            func.setId(400+i);
            if (delta != 0) {
                if (ite > 0) {
                    double y0 = (function.with("x", BigDecimal.valueOf(x0)).eval()).doubleValue();
                    func.setText("     "+String.valueOf(y0) + "           ");
                    if (y0 != 0) {
                        double x1 = x0 + delta;
                        vXn.setText("     "+ String.valueOf(x1) + "           ");
                        double y1 = (function.with("x", BigDecimal.valueOf(x1)).eval()).doubleValue();
                        func.setText("     "+String.valueOf(y1) + "           ");
                        int cont = 1;
                        iters.setText("     "+String.valueOf(cont) + "           ");
                        LineGraphSeries<DataPoint> serie = new LineGraphSeries<>();
                        serie.appendData(new DataPoint(x1, y1), false, ite);
                        while (((y1 * y0) > 0) && (cont < ite)) {
                            x0 = x1;
                            y0 = y1;
                            x1 = x0 + delta;
                            vXn.setText("     "+ String.valueOf(x1) + "           ");
                            y1 = (function.with("x", BigDecimal.valueOf(x1)).eval()).doubleValue();
                            func.setText("     "+String.valueOf(y1) + "           ");
                            if (delta >= 0)
                                serie.appendData(new DataPoint(x1, y1), false, ite);
                            else {
                                // no se puede graficar funciones alrevez :(
                            }
                            cont++;
                            iters.setText("     "+String.valueOf(cont) + "           ");
                        }
                        fila.addView(iters);
                        fila.addView(vXn);
                        fila.addView(func);
                        table.addView(fila);
                        graph.addSeries(serie);
                        if (y1 == 0) {
                            graphPoint(x1, y1, PointsGraphSeries.Shape.POINT, graph, getActivity(), "#0E9577", true);
                            //System.out.println(x1 + " is a root");
                        } else if (y1 * y0 < 0) {
                            //System.out.println("[" + x0 + ", " + x1 + "] is an interval");
                        } else {
                            // System.out.println("Failed the interval!");
                        }
                    } else {
                        graphPoint(x0, y0, PointsGraphSeries.Shape.POINT, graph, getActivity(), "#0E9577", true);
                        //System.out.println(x0 + " is a root");
                    }
                } else {
                    iter.setError("Iterate needs be >0");
                }
            } else {
                this.delta.setError("Delta cannot be zero");
            }
            num_celda = num_celda + 3;
        }

    }
