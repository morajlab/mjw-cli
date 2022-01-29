import options from "@morajlab/npm.config.nextjs";
import { IPluginProps } from "@morajlab/npm.mjw.types";

export default (config_callback: any) => {
  console.log(
    config_callback({
      plugins: [
        {
          name: "nextjs",
          options,
        } as IPluginProps,
      ],
    })
  );
};
