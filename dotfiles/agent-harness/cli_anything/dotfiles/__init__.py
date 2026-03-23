import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dotfiles running')
@cli.command()
def start(): click.echo('dotfiles started')
if __name__ == '__main__': cli()
