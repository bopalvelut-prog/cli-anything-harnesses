import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jack running')
@cli.command()
def start(): click.echo('jack started')
if __name__ == '__main__': cli()
