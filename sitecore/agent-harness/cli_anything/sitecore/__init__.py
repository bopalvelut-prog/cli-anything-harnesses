import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Sitecore running')
@cli.command()
def content(): click.echo('Sitecore content')
if __name__ == '__main__': cli()
