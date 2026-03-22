import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Zabbix server running')
@cli.command()
def hosts(): click.echo('Monitored hosts')
if __name__ == '__main__': cli()
