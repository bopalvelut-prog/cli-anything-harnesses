import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def beacon(): click.echo('Nimbus beacon')
@cli.command()
def validator(): click.echo('Nimbus validator')
if __name__ == '__main__': cli()
