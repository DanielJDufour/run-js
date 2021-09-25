// a more secure way to check that a module exists
// than executing a shell script

// check that this file is being run directly
// vs being accidentally imported
if (require.main === module) {
  // we store the module_name as a string
  let module_name = "";

  // if for some weird reason, the module name is super long
  // we might have multiple readable events
  process.stdin.on("readable", () => {
    const chunk = process.stdin.read();
    if (chunk !== null) {
      module_name += chunk;
    }
  });

  process.stdin.on("end", async () => {
    try {
      require.resolve(module_name);
      process.exit(0);
    } catch (error) {
      process.exit(1);
    }
  });
}
