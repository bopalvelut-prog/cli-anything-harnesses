import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Juniper router running')
@cli.command()
def interfaces(): click.echo('Network interfaces')
if __name__ == '__main__': cli()
