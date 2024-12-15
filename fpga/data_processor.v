module data_processor (
    input wire clk,
    input wire [31:0] data_in,
    input wire valid_in,
    output reg [31:0] data_out,
    output reg valid_out
);

always @(posedge clk) begin
    if (valid_in) begin
        data_out <= data_in * 2;  // Doubles the input
        valid_out <= 1;
    end else begin
        valid_out <= 0;
    end
end

endmodule

