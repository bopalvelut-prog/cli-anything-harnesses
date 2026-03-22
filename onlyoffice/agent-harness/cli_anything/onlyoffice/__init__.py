import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('OnlyOffice running')
@cli.command()
def docs(): click.echo('OnlyOffice docs')
if __name__ == '__main__': cli()
