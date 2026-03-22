import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def conversations(): click.echo('Drift conversations')
@cli.command()
def playbooks(): click.echo('Drift playbooks')
if __name__ == '__main__': cli()
