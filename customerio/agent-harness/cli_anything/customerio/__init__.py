import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def customers(): click.echo('Customer.io customers')
@cli.command()
def campaigns(): click.echo('Customer.io campaigns')
if __name__ == '__main__': cli()
