import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def swap(): click.echo('Orca swap')
@cli.command()
def pool(): click.echo('Orca pool')
if __name__ == '__main__': cli()
