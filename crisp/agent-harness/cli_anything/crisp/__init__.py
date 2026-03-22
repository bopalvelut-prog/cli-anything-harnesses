import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def conversations(): click.echo('Crisp conversations')
@cli.command()
def contacts(): click.echo('Crisp contacts')
if __name__ == '__main__': cli()
