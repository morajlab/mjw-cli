import path from "path";

export class Parser {
  private config_path: string;

  constructor(root: string) {
    this.config_path = path.join(root, "mjw.config.ts");
  }

  parse = async () => {
    try {
      const config_callback = await import(this.config_path);

      return config_callback.default;
    } catch (e) {
      console.log(e);
    }
  };
}

export default Parser;
