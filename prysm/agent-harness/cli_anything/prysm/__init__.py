import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def beacon(): click.echo('Prysm beacon')
@cli.command()
def validator(): click.echo('Prysm validator')
if __name__ == '__main__': cli()
