// check that this file is being run directly
// vs being accidentally imported
if (require.main === module) {
  let data = "";

  // if you passing a lot of data into the function
  // then we might have multiple readable events
  process.stdin.on("readable", () => {
    const chunk = process.stdin.read();
    if (chunk !== null) {
      data += chunk;
    }
  });

  process.stdin.on("end", async () => {
    try {
      const { boundary, module_name, function_name, params } = JSON.parse(data);

      const module = require(module_name);

      let func;
      if (function_name === "default") {
        if (typeof module === "function") {
          func = module;
        }
      } else {
        func = module[function_name];
      }

      const result = await Promise.resolve(func(...params));
      const str = JSON.stringify(result);
      const out = boundary + str;
      process.stdout.write(out);
      process.exit(0);
    } catch (error) {
      console.error(error);
      process.exit(1);
    }
  });
}
