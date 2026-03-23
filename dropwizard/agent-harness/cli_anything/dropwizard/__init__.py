import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dropwizard running')
@cli.command()
def start(): click.echo('dropwizard started')
if __name__ == '__main__': cli()
