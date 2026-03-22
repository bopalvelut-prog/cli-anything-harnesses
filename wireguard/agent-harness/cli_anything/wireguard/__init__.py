import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def up(): subprocess.run(['wg-quick', 'up', 'wg0'])
@cli.command()
def down(): subprocess.run(['wg-quick', 'down', 'wg0'])
@cli.command()
def show(): subprocess.run(['wg', 'show'])
@cli.command()
@click.argument('interface')
def genkey(interface): subprocess.run(['wg', 'genkey'], capture_output=True)
if __name__ == '__main__': cli()
