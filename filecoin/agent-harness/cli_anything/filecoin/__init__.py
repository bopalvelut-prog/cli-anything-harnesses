import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Filecoin status')
@cli.command()
def deal(): click.echo('Filecoin deal')
if __name__ == '__main__': cli()
