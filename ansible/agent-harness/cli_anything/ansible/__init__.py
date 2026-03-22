import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('inventory')
@click.argument('pattern')
def ping(inventory, pattern): subprocess.run(['ansible', '-i', inventory, pattern, '-m', 'ping'])
@cli.command()
@click.argument('playbook')
def play(playbook): subprocess.run(['ansible-playbook', playbook])
if __name__ == '__main__': cli()
