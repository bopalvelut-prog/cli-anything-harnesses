import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Umbraco running')
@cli.command()
def content(): click.echo('Umbraco content')
if __name__ == '__main__': cli()
