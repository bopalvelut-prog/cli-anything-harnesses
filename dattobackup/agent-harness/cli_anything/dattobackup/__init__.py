import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Datto status')
@cli.command()
def backup(): click.echo('Datto backup')
if __name__ == '__main__': cli()
