import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['falco'])
@cli.command()
def rules(): subprocess.run(['falco', '--list', 'all_rules'])
if __name__ == '__main__': cli()
