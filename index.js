const fs = require('node:fs');
const path = require('node:path');
const { Client, Collection, Events, GatewayIntentBits } = require('discord.js');

require('dotenv').config();
const token = process.env.BOT_TOKEN;

const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.commands = new Collection(); // Collection, key as command name and value as exported module
const foldersPath = path.join(__dirname, 'commands');
const commandFolders = fs.readdirSync(foldersPath);

// Add all script from commands folder
for (const folder of commandFolders) {
	const commandsPath = path.join(foldersPath, folder);
	const commandFiles = fs.readdirSync(commandsPath).filter(file => file.endsWith('.js'));
    // Loop through all command folders
	for (const file of commandFiles) {
        // Loop through all command files
		const filePath = path.join(commandsPath, file);
		const command = require(filePath);
		if ('data' in command && 'execute' in command) {
            // Add command to collection
			client.commands.set(command.data.name, command);
		} else {
            // Missing required properties
			console.log(`[WARNING] The command at ${filePath} is missing a required "data" or "execute" property.`);
		};
	};
};

// Receive command interactions
client.on(Events.InteractionCreate, async interaction => {
	if (!interaction.isChatInputCommand()) return; // Filter to only have slash commands

	const command = interaction.client.commands.get(interaction.commandName);

    // Check if command exists
	if (!command) {
        // Command not found
		console.error(`No command matching ${interaction.commandName} was found.`);
		return;
	}

    // Error-handling
	try {
		await command.execute(interaction);
	} catch (error) {
		console.error(error);
		if (interaction.replied || interaction.deferred) {
			await interaction.followUp({ content: 'There was an error while executing this command!', ephemeral: true });
		} else {
			await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
		}
	}
});

// Bot online
client.once(Events.ClientReady, readyClient => {
	console.log(`Ready! Logged in as ${readyClient.user.tag}`);
});

// Log in to Discord
client.login(token);