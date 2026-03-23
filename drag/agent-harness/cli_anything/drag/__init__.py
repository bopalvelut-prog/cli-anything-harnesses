import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('drag running')
@cli.command()
def start(): click.echo('drag started')
if __name__ == '__main__': cli()
