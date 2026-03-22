import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('IDrive status')
@cli.command()
def backup(): click.echo('IDrive backup')
if __name__ == '__main__': cli()
