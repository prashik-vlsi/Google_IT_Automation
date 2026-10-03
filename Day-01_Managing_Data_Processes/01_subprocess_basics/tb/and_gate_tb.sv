`timescale 1ns/1ps

module and_gate_tb;

    logic a;
    logic b;
    logic y;

    and_gate dut (
        .a(a),
        .b(b),
        .y(y)
    );

    initial begin

        $display("Starting AND gate verification");

        a = 0; b = 0;
        #10;
        $display("a=%b b=%b y=%b", a, b, y);

        a = 0; b = 1;
        #10;
        $display("a=%b b=%b y=%b", a, b, y);

        a = 1; b = 0;
        #10;
        $display("a=%b b=%b y=%b", a, b, y);

        a = 1; b = 1;
        #10;
        $display("a=%b b=%b y=%b", a, b, y);

        $display("Verification completed");

        $finish;
    end

endmodule