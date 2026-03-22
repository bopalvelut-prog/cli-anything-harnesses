import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def beacon(): click.echo('Lighthouse beacon')
@cli.command()
def validator(): click.echo('Lighthouse validator')
if __name__ == '__main__': cli()
