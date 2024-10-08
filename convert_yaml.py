print("———————— [script] ————————")
print("executing yaml to ts language configuration file conversion")

import yaml
import json
from pathlib import Path

src = Path('./src/parser/data/languageConfig.yaml')
dst=Path('./src/languageConfig.ts')

# Load YAML file
with open(src, 'r') as file:
    yaml_data = yaml.safe_load(file)
    
# Convert YAML data to JSON
json_data = json.dumps({"language" : yaml_data["language"]}, indent=4)


# Convert JSON data to TypeScript
ts_data = 'export const data = `' + json_data + '`;'

# Write TypeScript file
with open(dst, 'w') as file:
    file.write(ts_data)
    
# Read the file into a list of lines
with open(dst, 'r') as file:
    lines = file.readlines()

# Replace the first line
lines[0] = """interface LanguageConfig {
    // must have at least one of these
    delimiter?: string;
    commentFormat?: string[];
    escapeRegExp?: string;
    // if needed
    highlightJSDoc?: boolean;
    // always has a value
    ignoreFirstLine: boolean;
    isPlainText: boolean;
    supportedLanguage: boolean;
}

interface Config {
    language: Record<string, LanguageConfig>;
}

export const doc : Config = {
"""

# Replace the last line
lines[-1] = '};\n'

# Write the list back to the file
with open(dst, 'w') as file:
    file.writelines(lines)
    print(f"converted {src} to {dst}")

print("———————— script ends here ————————")