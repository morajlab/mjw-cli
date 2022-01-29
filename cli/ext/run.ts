import { Parser } from "./parser";

class Run {
  private command: string;
  private root: string;
  private extra: string[];
  private parser: Parser;

  constructor(args: string[]) {
    this.command = args[0];
    this.root = args[2];
    this.extra = args.slice(3);
    this.parser = new Parser(this.root);
  }

  run = async () => {
    try {
      const command = await import(`../plugins/${this.command}`);
      const config_callback = await this.parser.parse();

      command.default(config_callback);
    } catch (e) {
      console.log(`ERROR: command '${this.command}' doesn't exist.`);
    }
  };
}

const runner = new Run(process.argv.slice(2));
runner.run();
