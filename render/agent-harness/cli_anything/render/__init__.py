import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def deploy(): click.echo('Deploy to Render')
@cli.command()
def status(): click.echo('Render status')
if __name__ == '__main__': cli()
